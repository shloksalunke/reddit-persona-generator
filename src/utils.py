def save_persona_to_file(username: str, persona_text: str, output_folder: str = "output"):
    output_path = f"{output_folder}/{username}_persona.txt"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(persona_text)
    print(f"✅ Persona saved at: {output_path}")
