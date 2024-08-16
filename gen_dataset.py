import json
from datasets import Dataset

# Single-turn QA
single_turn_qa = [
    {
        "question": "How can I truly achieve self-identification and enhance self-efficacy?",
        "answer": "Self-identification is a complex process that involves gradually building a positive self-assessment. As mentioned in 'Everything I Never Told You': 'We spend our whole lives trying to escape the expectations of others and find our true selves.' To enhance self-efficacy, focus on your strengths, set realistic goals, and practice self-acceptance. Remember, it's about viewing yourself objectively and truthfully, and handling the relationship between the self and the outside world rationally."
    },
    {
        "question": "I'm struggling with anxiety. What can I do to manage it?",
        "answer": "Managing anxiety involves several strategies. First, practice deep breathing exercises or meditation to help calm your mind. Regular exercise can also reduce anxiety symptoms. Consider keeping a journal to identify triggers and patterns. Cognitive-behavioral therapy (CBT) techniques can be helpful in challenging negative thought patterns. If anxiety is significantly impacting your daily life, consider speaking with a mental health professional for personalized strategies and potential treatment options."
    }
]

# Multi-turn dialogue
multi_turn_dialogue = [
    {
        "dialogue": [
            {"role": "user", "content": "I feel like I can never truly accept myself. Sometimes I think I've done quite a few good things, but deep down, I still can't accept myself, which makes me feel very troubled."},
            {"role": "assistant", "content": "Hello, I can sense your struggle, and it must not be easy. Self-identification is indeed a complex and profound journey. In this process, I am here to support you, and together we can explore how to gradually build a positive self-assessment. As stated in 'Everything I Never Told You': 'We spend our whole lives trying to escape the expectations of others and find our true selves.'"},
            {"role": "user", "content": "I have tried to focus on my strengths, but I always feel that those strengths are not enough to make me feel proud. It seems that I am always dissatisfied with my achievements; how should I adjust this mindset?"},
            {"role": "assistant", "content": "I understand how you feel; the pursuit of perfection is a natural human instinct, but excessively high expectations can sometimes lead to frustration. Let's take it step by step, you've already done very well. I suggest you try to adjust your expectations and set more realistic and achievable goals. Remember, establishing self-identity requires us to view ourselves objectively and truthfully, and to handle the relationship between the self and the outside world rationally."}
        ]
    }
]

# Knowledge-based QA
knowledge_qa = [
    {
        "question": "What is cognitive dissonance in psychology?",
        "answer": "Cognitive dissonance is a psychological concept that refers to the mental discomfort experienced when a person holds two or more contradictory beliefs, ideas, or values simultaneously. This discomfort leads to an inner drive to reduce the dissonance by modifying existing beliefs, adding new ones to create a consistent belief system, or reducing the importance of any of the dissonant elements. It was first proposed by Leon Festinger in 1957 and has been widely studied in social psychology."
    },
    {
        "question": "Explain the concept of 'self-efficacy' in psychology.",
        "answer": "Self-efficacy is a concept in psychology developed by Albert Bandura. It refers to an individual's belief in their capacity to execute behaviors necessary to produce specific performance attainments. In other words, it's a person's confidence in their ability to succeed in specific situations or accomplish a task. Self-efficacy can have a strong influence on how people approach goals, tasks, and challenges. High self-efficacy can enhance a person's resilience, problem-solving abilities, and overall well-being."
    }
]

# Combine all data
all_data = (
    [{"type": "single_turn_qa", **item} for item in single_turn_qa] +
    [{"type": "multi_turn_dialogue", **item} for item in multi_turn_dialogue] +
    [{"type": "knowledge_qa", **item} for item in knowledge_qa]
)

# Create a Hugging Face Dataset
dataset = Dataset.from_list(all_data)

# Save the dataset to a JSON file
with open('psych_dataset_demo.json', 'w', encoding='utf-8') as f:
    json.dump(all_data, f, ensure_ascii=False, indent=2)

print("Dataset created and saved as 'psych_dataset_demo.json'")
print("Dataset statistics:")
print(dataset)