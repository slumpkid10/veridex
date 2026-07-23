from core.engine import VeridexEngine
from hunters.reddit_pipeline import RedditPipeline


def main():
    print("🚀 Starting VERIDEX...")

    engine = VeridexEngine()
    engine.start()

    pipeline = RedditPipeline()

    pipeline.process_post(
        "Need urgent WordPress developer to fix my website",
        client="Demo Client",
        budget=150,
    )

    print("✅ VERIDEX Test Completed")


if __name__ == "__main__":
    main()
