from django.conf import settings
from groq import Groq


def analyze_job_description(job_description):
    if not settings.GROQ_API_KEY:
        raise ValueError("Groq API key is not configured.")

    if not job_description or not job_description.strip():
        raise ValueError("Job description cannot be empty.")

    client = Groq(
        api_key=settings.GROQ_API_KEY,
        max_retries=2,
        timeout=30.0,
    )

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a professional job description analyzer. "
                    "Analyze the provided job description. "
                    "Return a clean breakdown using these exact HTML tags or markdown headings so they can be styled: "
                    "### Summary\n"
                    "### Required Skills\n"
                    "### Technologies and Tools\n"
                    "### Experience Requirements\n"
                    "### Interview Preparation Topics"
                ),
            },
            {
                "role": "user",
                "content": job_description,
            },
        ],
    )

    analysis = response.choices[0].message.content
    return analysis