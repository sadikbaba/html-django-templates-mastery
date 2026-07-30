from faker import Faker

fake = Faker()


def generate_form_data(count=5):
    print("=== Fake Event Registration Data ===\n")

    for i in range(1, count + 1):
        print(f"Submission #{i}")
        print(f"Name       : {fake.name()}")
        print(f"Email      : {fake.email()}")
        print(f"Phone      : {fake.phone_number()}")
        print(f"Experience : {fake.random_element(elements=('Beginner', 'Intermediate', 'Advanced'))}")
        print(f"Skills     : {', '.join(fake.words(nb=3))}")
        print(f"Message    : {fake.sentence()}")
        print("-" * 40)
        print(f"Skills     : {', '.join(fake.random_elements(elements=('HTML', 'CSS', 'JavaScript', 'Python', 'Django', 'AI'), length=3, unique=True))}")

# Generate 5 fake form submissions
generate_form_data(5)


  