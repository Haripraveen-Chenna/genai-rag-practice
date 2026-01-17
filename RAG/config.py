from pathlib import Path

DATA_DIR = Path("data")

EMBEDDING_MODEL = "all-MiniLM-L6-v2"
GEN_MODEL = "google/flan-t5-base"

MIN_CHUNK_LENGTH = 200
TOP_K = 5

# ✏️ CHANGE THESE BASED ON YOUR PDFs
HEADINGS = [
    "Introduction",
    "Background and Context",
    "Definition of Child Care",
    "Importance of Early Childhood Care",
    "Types of Child Care Arrangements",
    "Child Development and Learning",
    "Health, Safety, and Nutrition",
    "Role of Parents and Caregivers",
    "Access and Affordability",
    "Quality of Child Care Services",
    "Challenges and Constraints",
    "Government Policies and Programs",
    "Best Practices and Recommendations",
    "Impact on Children and Families",
    "Future Directions",
    "Conclusion"
]

