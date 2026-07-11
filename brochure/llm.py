import json

from dotenv import load_dotenv
from openai import OpenAI

from brochure.scraper import fetch_website_contents, fetch_website_links
from brochure.prompts import LINK_SYSTEM_PROMPT, BROCHURE_SYSTEM_PROMPT, link_user_prompt, brochure_user_prompt

MODEL = "gpt-4o-mini"

class LLM:
    def __init__(self):
        load_dotenv(override=True)
        self.client = OpenAI()

    def fetch_relevant_links(self, url):
        links = fetch_website_links(url).links
        response = self.client.chat.completions.create(
            model=MODEL,
            response_format={"type": "json_object"},
            messages=[
                {"role": "system", "content": LINK_SYSTEM_PROMPT},
                {"role": "user", "content": link_user_prompt(url, links)},
            ],
        )
        result = response.choices[0].message.content
        return json.loads(result)["links"]

    def fetch_page_and_all_relevant_links(self, url):
        landing = fetch_website_contents(url)
        result = f"## Landing Page:\n\n{landing.title}\n{landing.body}\n## Relevant Links:\n"
        for link in self.fetch_relevant_links(url)[:3]:
            page = fetch_website_contents(link["url"])
            result += f"\n\n### Link: {link['type']}\n{page.title}\n{page.body}"
        return result

    def generate_brochure(self, company_name, url):
        contents = self.fetch_page_and_all_relevant_links(url)
        response = self.client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": BROCHURE_SYSTEM_PROMPT},
                {"role": "user", "content": brochure_user_prompt(company_name, contents)},
            ],
        )
        return response.choices[0].message.content


if __name__ == "__main__":
    llm = LLM()
    brochure = llm.generate_brochure("Example Company", "https://example.com")
    print(brochure)
