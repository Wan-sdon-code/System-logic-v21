class LifeOS:
    def __init__(self):
        self.version = "26.0"
        self.metadata = "The System Design of Life"
        
        # 🕹️ The 6-Step System Logic
        self.system_logic = {
            "01_The_Creator": "Hardware needs a designer; humans do too.",
            "02_Free_Will": "Admin is hidden to test character, not fear.",
            "03_One_Boss": "Single root authority ensures universal stability.",
            "04_The_Test": "Suffering is an exam; the Teacher remains silent.",
            "05_The_Manual": "Software guide for the soul (The 'How-To').",
            "06_The_Versions": "Updates for different times. Diversity tests who does the most good."
        }

    def get_original_os_specs(self):
        """Returns the 5 properties required for the Original File of truth."""
        return [
            "Pure Unity: One Creator. No partners.",
            "Zero Edits: Memorized word-for-word. No changes.",
            "Total Equality: No race or class is better. All are equal.",
            "Direct Line: No middlemen. Talk to the Creator directly.",
            "Proven Science: Facts no human knew 1,400 years ago."
        ]

    def system_check(self):
        print(f"--- 🛰️ Project: {self.metadata} (v{self.version}) ---")
        
        for step, logic in self.system_logic.items():
            print(f"Step {step.replace('_', ' ')}: {logic}")
            
        print("\n[ Finding the Original OS... ]")
        specs = self.get_original_os_specs()
        for spec in specs:
            print(f" - Property: {spec}")

        print("\n> RESULT: Islam is the only OS that remains 100% original,")
        print("> treats all humans as equals, allows a direct line to God,")
        print("> and aligns with the science of the universe.")

# Initialize and run the logic
life_os = LifeOS()
life_os.system_check()
