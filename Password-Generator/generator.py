import string
import secrets

class PasswordGenerator:
    def __init__(self, length: int, include_upper: bool, include_lower: bool, include_num: bool, include_symbols: bool):
        """
        Initialize the password generator with user preferences.
        
        Args:
            length (int): Desired length of the password.
            include_upper (bool): Include uppercase letters.
            include_lower (bool): Include lowercase letters.
            include_num (bool): Include digits.
            include_symbols (bool): Include special characters.
        """
        self.length = length
        self.include_num = include_num
        self.include_symbols = include_symbols
        self.include_upper = include_upper
        self.include_lower = include_lower

        # Dictionary of available character sets
        self.char_sets = {
            "upper": string.ascii_uppercase,
            "lower": string.ascii_lowercase,
            "num": string.digits,
            "symbols": "!@#$%^&*()"
        }

        # Validate that at least one character set is selected
        self._validate_inputs()

    def _validate_inputs(self):
        """Raise an error if no character sets are selected."""
        if not (self.include_upper or self.include_lower or self.include_num or self.include_symbols):
            raise ValueError("At least one character type must be selected.")

    def generate_password(self):
        """
        Generate a secure password based on the selected options.
        Ensures at least one character from each selected type is included.
        
        Returns:
            str: The generated password.
        """
        selected_char = []  # Holds guaranteed characters from each selected set
        pool = ""           # Combined pool of all allowed characters

        # Add at least one character from each selected type and build the pool
        if self.include_num:
            pool += self.char_sets["num"]
            selected_char.append(secrets.choice(self.char_sets["num"]))

        if self.include_symbols:
            pool += self.char_sets["symbols"]
            selected_char.append(secrets.choice(self.char_sets["symbols"]))

        if self.include_upper:
            pool += self.char_sets["upper"]
            selected_char.append(secrets.choice(self.char_sets["upper"]))
            
        if self.include_lower:
            pool += self.char_sets["lower"]
            selected_char.append(secrets.choice(self.char_sets["lower"]))
            
        # Calculate how many additional characters are needed
        remaining_length = self.length - len(selected_char)

        # Fill the rest of the password with random choices from the full pool
        selected_char += [secrets.choice(pool) for _ in range(remaining_length)]

        # Shuffle the final password to ensure randomness
        secrets.SystemRandom().shuffle(selected_char)

        # Convert list to string
        password = "".join(selected_char)

        # Save to local file and return the password
        self.save_to_device(password)
        return password

    @staticmethod
    def save_to_device(password: str):
        """
        Save the generated password to a local text file.
        
        Args:
            password (str): The password to save.
        """
        with open("password.txt", "w") as file:
            file.write(password)