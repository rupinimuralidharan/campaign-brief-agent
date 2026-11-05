<img width="1585" height="921" alt="Screenshot 2026-11-05 234119" src="https://github.com/user-attachments/assets/38f4c37a-28c2-45b9-951b-ef7d7cf9297c" />
<img width="1590" height="971" alt="Screenshot 2026-11-05 234047" src="https://github.com/user-attachments/assets/3e9445ec-20e2-4d22-b7d7-544db74eac27" />
# campaign-brief-agent
AI agent that generates structured mock campaign briefs, built on my digital marketing playbook
# Campaign Brief Generator: an AI agent built on my digital marketing playbook

**Hi, I'm Rupini, a digital marketer specialising in performance marketing, growth marketing, CRM & lifecycle, social media marketing and community management.** I'm GA4 certified, AI-Powered Performance Ads certified, and hold an MSc in Digital Marketing.

This repo is an AI agent I built with Google Cloud Agent Studio. It turns the way I plan campaigns into a tool: give it a product, an audience and a budget, and it returns a structured campaign brief.

---

## What it does

1. Takes a product, target audience and budget.
2. Asks clarifying questions if critical details are missing, the way I would with a client.
3. Produces a brief with seven sections:
   - **Objective:** specific, measurable goals
   - **Target audience:** demographics, behaviours, pain points
   - **Positioning:** value proposition and messaging angles
   - **Channels and budget split:** percentages and exact amounts
   - **KPIs:** numeric targets
   - **30-day plan:** week by week
   - **Risks:** what could go wrong and how to mitigate it
4. Can search the web and read URLs to ground its recommendations.

## Example

**Prompt:** *Plan a launch campaign for a D2C skincare brand on Instagram with a €5,000 budget, targeting women 25-40 in Germany.*

> Note: benchmark figures (CPM, CTR, CAC, ROAS) in the output are estimates, not guarantees. They should be checked against your own account data.

## Selected work that shaped this agent

### [Brand or "D2C skincare brand"]
- **Challenge:** 
- **What I did:** 
- **Result:** 
- **Lesson:** 

## How it's built

- **Platform:** Google Cloud Agent Studio, exported as code
- **Framework:** Google Agent Development Kit (ADK) in Python
- **Model:** Gemini
- **Tools:** Google Search and URL context, each as a sub-agent
- **Logic:** the marketing method lives in the agent's instructions (see `agent.py`)

## Running it yourself

This agent uses Google Cloud, so you need your own project and credentials:

```bash
pip install -r requirements.txt
```

You'll also need a Google Cloud project with Vertex AI enabled and authentication set up. See the [ADK documentation](https://google.github.io/adk-docs/) for how to run an exported agent.

## About me

Marketer first, builder second. I created this project to show how marketing expertise can be turned into practical AI tools.
