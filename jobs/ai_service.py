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
                    "Analyze only the provided job description. "
                    "Do not invent requirements that are not mentioned. "
                    "Return a clear, structured analysis with these headings: "
                    "Summary, Required Skills, Technologies and Tools, "
                    "Experience Requirements, Interview Preparation Topics."
                ),
            },
            {
                "role": "user",
                "content": job_description,
            },
        ],
    )

    analysis = response.choices[0].message.content

    if not analysis:
        raise ValueError("Groq returned an empty response.")

    return analysis