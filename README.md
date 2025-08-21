# Tabla de Contenidos

11. [Building and managing artifacts](#building-and-managing-artifacts)

---

## Building and managing artifacts
![Imagen de GitHub](https://github.com/ariegd/automate/blob/04_03/src/img/Captura%20desde%202025-08-21%2020-06-10.png)
![Imagen de GitHub](https://github.com/ariegd/automate/blob/04_03/src/img/Captura%20desde%202025-08-21%2020-06-47.png)


## como crear ${{ secrets.GCP_SERVICE_ACCT_EMAIL }} en github


Creating a GitHub secret for your GCP service account email is a straightforward process. Here's a step-by-step guide on how to do it:

1. Navigate to your GitHub Repository
First, go to the GitHub repository where you want to use this secret.

2. Access Repository Settings
Click on the "Settings" tab at the top of the repository page.

3. Go to the Secrets and Variables Section
In the left-hand sidebar, find and click on "Secrets and variables". From the dropdown menu, select "Actions".

4. Create a New Repository Secret
On the "Actions secrets" page, click the "New repository secret" button.

5. Define the Secret
Name: In the "Name" field, enter GCP_SERVICE_ACCT_EMAIL. It's crucial that the name matches exactly with what you use in your workflow files.

Secret: In the "Secret" field, paste the actual email address of your GCP service account.

Once you have entered the name and the value, click "Add secret".

That's it! Your GCP_SERVICE_ACCT_EMAIL secret is now available for use in your GitHub Actions workflows as ${{ secrets.GCP_SERVICE_ACCT_EMAIL }}.
