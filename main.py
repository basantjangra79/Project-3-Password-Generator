
# Password Generator

import string
import secrets

print("\nWelcome to Password Generator!")

while True:
    try: 

        pass_length = int(input("\nEnter Password Length: "))

        while True:
            try:
                lower_case = string.ascii_lowercase
                upper_case = string.ascii_uppercase
                digits = string.digits
                special_chars = "@#$%&*_-+=!"

                password = [
                    secrets.choice(lower_case),
                    secrets.choice(upper_case),
                    secrets.choice(digits),
                    secrets.choice(special_chars)
                ]

                all_chars = lower_case + upper_case + digits + special_chars

                password.extend(
                    secrets.choice(all_chars) 
                    for _ in range(pass_length - 4)
                )

                secrets.SystemRandom().shuffle(password)
                password = "".join(password)

                print(f"Your Password: {password}")

                print("\n" + "="*40 + " Coded by: Basant Jangra " + "="*40)

                re_generate = input("\nWants to Re-Generate Password ? [y/n]: ")

                if re_generate == "y":
                    continue

                else:
                    print("\nRedirecting to Main Menu...")
                    break

            except KeyboardInterrupt:
                print("\nRedirecting to Main Menu...")
                break
            
    
    except KeyboardInterrupt:
        print("\n\nProgram Closed by User.")
        break

    except ValueError:
        print("\nInvalid Value! Enter Value as per Requested Format Only.")
        continue
