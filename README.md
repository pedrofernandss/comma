# Turinguinho

<div style="text-align: center;">
  <img src="./assets/turinguinho_image.png" alt="Turinguinho" width="300"/>
</div>


Turinguinho is a little robot inspired by Alan Turing. It shares texts, articles, news, and features from different sources designed to challenge conventional thinking about the world of Artificial Intelligence and Computing and its impact on society, culture and business.

## 🚀 How to Run the Project

To get Turinguinho up and running, follow these steps:

1.  **Set up Environment Variables:**
    * Copy the `.env.example` file to a new file named `.env`:
  
        ```bash
        cp .env.example .env
        ```
    * Open the `.env` file and add the values for the following variables:
  
        * `DISCORD_CHANNEL_ID`: The ID of the Discord channel where the bot will post.
        * `DISCORD_TOKEN`: Your Discord bot token.

2.  **Create and Activate a Virtual Environment (venv):**
    * Create the virtual environment (if you don't already have a `venv` directory):
    
        ```bash
        python -m venv venv
        ```
    * Activate the virtual environment:
        * On Windows (cmd.exe):

            ```bash
            .\venv\Scripts\activate
            ```
        * On Windows (PowerShell):

            ```powershell
            .\venv\Scripts\Activate.ps1
            ```
        * On macOS and Linux:

            ```bash
            source venv/bin/activate
            ```

3.  **Install Dependencies:**
    * With the virtual environment activated, install all the necessary libraries listed in the `requirements.txt` file:

        ```bash
        pip install -r requirements.txt
        ```

All set! After this, you should be able to run the main project script. 🎉

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

### How to Contribute

1.  **Fork the Project**
    * Click the 'Fork' button at the top right of the main repository page. This creates your own copy of the project.

2.  **Clone Your Fork**
    * Clone your forked repository to your local machine:

      ```bash
      git clone [https://github.com/pedrofernandss/turinguinho.git](https://github.com/pedrofernandss/turinguinho.git) 
      ```

3.  **Create your Feature Branch**
    * Navigate to your local repository directory and create a new branch for your changes:

      ```bash
      git checkout -b feature/AmazingFeature
      ```
      (Name your branch something descriptive, like `fix/TypoInReadme` or `feature/NewDataSource`)

4.  **Make your Changes**
    * Implement your fixes or new features.
    * Ensure your code follows any existing style guidelines (if any).

5.  **Commit your Changes**
    * Stage and commit your changes with a clear and concise commit message:

      ```bash
      git add .
      git commit -m 'Add some AmazingFeature'
      ```

6.  **Push to your Branch**
    * Push your changes up to your forked repository on GitHub:
      ```bash
      git push origin feature/AmazingFeature
      ```

7.  **Open a Pull Request**
    * Go to your repository on GitHub. You should see a prompt to create a Pull Request from your new branch.
    * Click on it, review your changes, and write a clear title and description for your Pull Request, explaining the changes you've made.
    * Click 'Create Pull Request'.

### Reporting Bugs

If you find a bug, please open an issue on GitHub.
* Clearly describe the bug, including steps to reproduce it.
* Mention your operating system and relevant software versions (like Python version).
* Include any error messages or screenshots if applicable.

### Suggesting Enhancements

If you have an idea for a new feature or an improvement to an existing one:
* Open an issue on GitHub.
* Clearly describe the enhancement and why you think it would be beneficial.
* You can also discuss your ideas before starting to work on a Pull Request.