#!/usr/bin/env python3

class LakshyaVerma:
    def __init__(self):
        self.name = "Lakshya Verma"
        self.role = "Civil Engineering Student @ IIT Bhubaneswar"
        self.goal = "Software Engineer"

        self.currently_building = [
            "Python Projects",
            "Data Structures & Algorithms"
        ]

        self.learning = [
            "Python",
            "DSA",
            "SQL",
            "Git",
            "GitHub",
            "Object-Oriented Programming"
        ]

        self.open_to_collaborate = [
            "Python",
            "Open Source",
            "Automation Projects"
        ]

        self.seeking_guidance = [
            "Backend Development",
            "REST APIs",
            "Cloud Technologies"
        ]

        self.ask_me_about = [
            "Python",
            "Git",
            "GitHub",
            "Competitive Programming"
        ]

        self.socials = {
            "LinkedIn": "linkedin.com/in/lakshya-verma07",
            "Instagram": "instagram.com/lakshya._.verma",
            "X": "x.com/lakshya_716",
            "Email": "lakshyaverma07012006@gmail.com"
        }

        self.tech_stack = {
            "Languages": ["Python", "Java", "C", "JavaScript"],
            "Tools": ["Git", "GitHub"],
            "Currently_Focusing_On": [
                "Problem Solving",
                "Backend Development",
                "Open Source"
            ]
        }

        self.fun_fact = (
            "I enjoy turning ideas into Python projects "
            "while preparing for Software Engineering placements."
        )


if __name__ == "__main__":
    me = LakshyaVerma()

    print("=" * 55)
    print(f"👋 Hi, I'm {me.name}")
    print(f"🎓 {me.role}")
    print(f"🎯 Goal: {me.goal}")
    print("=" * 55)

    print("\n🔭 Currently Building")
    for item in me.currently_building:
        print(f" • {item}")

    print("\n🌱 Learning")
    print(" • " + " • ".join(me.learning))

    print("\n👯 Open to Collaborate On")
    print(" • " + " • ".join(me.open_to_collaborate))

    print("\n🤝 Seeking Guidance In")
    print(" • " + " • ".join(me.seeking_guidance))

    print("\n💬 Ask Me About")
    print(" • " + " • ".join(me.ask_me_about))

    print("\n💻 Tech Stack")
    for category, skills in me.tech_stack.items():
        print(f" {category}: {', '.join(skills)}")

    print("\n🌐 Connect With Me")
    for platform, link in me.socials.items():
        print(f" {platform}: {link}")

    print(f"\n⚡ Fun Fact: {me.fun_fact}")

    print("\n📊 GitHub Stats")
    print("https://github-readme-stats.shion.dev/api?username=lakshya716")
    print("https://streak-stats.demolab.com/?user=lakshya716")
    print("https://github-profile-trophy.vercel.app/?username=lakshya716")

    print("\nprint('Thanks for visiting my profile! ⭐')")
