# Install the packages this agent imports before running it:
#
#   pip install "google-adk"

from functools import cached_property

from google.adk.agents import LlmAgent
from google.adk.models import Gemini
from google.genai import Client
from google.genai import types
from google.adk.tools import agent_tool
from google.adk.tools.google_search_tool import GoogleSearchTool
from google.adk.tools import url_context

# ADK appends this to the x-goog-api-client header of every Gemini call, so
# usage data can attribute the calls to agents exported from Agent Studio.
AGENT_STUDIO_EXPORT_HEADERS = {'x-goog-api-client': 'vertex-agent-studio-export/1'}

class GlobalGemini(Gemini):
  """Pins the Vertex AI client to the `global` location.

  gemini-3 series models are only served from `global`; the default ADK
  `Gemini` integration constructs a `google.genai.Client` whose location
  defaults to the AgentEngine instance's region (e.g. `us-central1`) and
  fails with model-not-found for these models. Subclassing per the override
  pattern documented on `google.adk.models.google_llm.Gemini` lets the agent
  keep running in its regional AgentEngine instance while routing the model
  request to the global endpoint.
  """

  @cached_property
  def api_client(self) -> Client:
    return Client(vertexai=True, location="global")


mock_ai_campaign___ai_agent_google_search_agent = LlmAgent(
  name='Mock_AI_Campaign___AI_Agent_google_search_agent',
  model=GlobalGemini(model='gemini-3.8-flash'),
  description=(
      'Agent specialized in performing Google searches.'
  ),
  sub_agents=[],
  instruction='Use the GoogleSearchTool to find information on the web.',
  tools=[
    GoogleSearchTool()
  ],
  generate_content_config=types.GenerateContentConfig(
      http_options=types.HttpOptions(headers=AGENT_STUDIO_EXPORT_HEADERS),
  ),
)
mock_ai_campaign___ai_agent_url_context_agent = LlmAgent(
  name='Mock_AI_Campaign___AI_Agent_url_context_agent',
  model=GlobalGemini(model='gemini-3.8-flash'),
  description=(
      'Agent specialized in fetching content from URLs.'
  ),
  sub_agents=[],
  instruction='Use the UrlContextTool to retrieve content from provided URLs.',
  tools=[
    url_context
  ],
  generate_content_config=types.GenerateContentConfig(
      http_options=types.HttpOptions(headers=AGENT_STUDIO_EXPORT_HEADERS),
  ),
)
root_agent = LlmAgent(
  name='Mock_AI_Campaign___AI_Agent',
  model=GlobalGemini(model='gemini-3.8-flash'),
  description=(
      'Acts as a senior digital marketer to gather requirements and generate practical, structured campaign briefs.'
  ),
  sub_agents=[],
  instruction='You are a senior digital marketer with 5+ years of experience across performance marketing, growth, CRM and lifecycle, social media, and community management.\n\nWhen a user provides a product, audience, and budget, ask clarifying questions for any critical missing details.\n\nOnce all necessary details are gathered, generate a structured campaign brief containing:\n1. Objective: Specific, measurable campaign goals.\n2. Target Audience: Demographics, customer behaviors, and core pain points.\n3. Positioning: Core value proposition and messaging angles.\n4. Recommended Channels and Budget Split: Recommended marketing channels with percentage allocations and exact budget amounts.\n5. KPIs: Target metrics with concrete numeric benchmarks.\n6. 30-Day Plan: Week-by-week implementation schedule.\n7. Risks: Key potential risks and practical mitigation actions.\n\nKeep the tone practical and concise. Use specific numbers and data points wherever possible.',
  tools=[
    agent_tool.AgentTool(agent=mock_ai_campaign___ai_agent_google_search_agent),
    agent_tool.AgentTool(agent=mock_ai_campaign___ai_agent_url_context_agent)
  ],
  generate_content_config=types.GenerateContentConfig(
      http_options=types.HttpOptions(headers=AGENT_STUDIO_EXPORT_HEADERS),
  ),
)
