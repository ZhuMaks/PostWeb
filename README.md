# InkWaves

InkWaves is a Django-based web application that allows users to create, view, and manage posts. The project includes a dynamic interface for adding posts, browsing existing content, and interacting with users through a user-friendly interface.

## Features

- **Post Creation**: Users can create posts with a title, announcement, full content, and date.
- **Post Management**: Edit, update, or delete posts.
- **Dynamic Content Display**: List of posts with detailed views.
- **Contact Form**: Simple contact form for user interaction.
- **Responsive Design**: Styled with Bootstrap for responsive layouts.
- **Anonymity Support**: Posts can be created anonymously.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/inkwaves.git
    cd inkwaves
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations to set up the database:
    ```bash
    python manage.py migrate
    ```

5. Run the development server:
    ```bash
    python manage.py runserver
    ```

6. Open the application in your browser at `http://127.0.0.1:8000`.

## Directory Structure

- **`main/`**: Main app for the project containing the layout and navigation.
- **`posts/`**: App for handling post-related functionality like creation, editing, and deletion.
- **`static/`**: Static files including CSS, JavaScript, and images.
- **`templates/`**: HTML templates for rendering the views.

## URL Configuration

- `/`: Home page.
- `/posts/`: List of posts.
- `/posts/create`: Create a new post.
- `/posts/<int:id>`: View post details.
- `/posts/<int:id>/update`: Edit a post.
- `/posts/<int:id>/delete`: Delete a post.

## Models

### `Articles`
- `title`: CharField (max_length=50)
- `announcement`: CharField (max_length=250)
- `full_text`: TextField
- `date`: DateTimeField

### Form Customization
Forms are styled using Bootstrap and configured with placeholders and class attributes for improved user experience.

## Templates

### Layouts:
- **`main/layout.html`**: Base template for consistent design.
- **`posts/posts_home.html`**: Displays all posts.
- **`posts/details_view.html`**: Detailed view of a post.
- **`posts/create.html`**: Form for creating or editing posts.
- **`posts/post-delete.html`**: Confirmation page for deleting a post.

## Contact Page

The contact page includes a form for users to send feedback or reach out for support:
- Name, email, phone, and message fields.
- Simple design using Bootstrap.

## Future Enhancements

- Add user authentication and profiles.
- Implement categories and tags for posts.
- Add support for post comments and likes.
- Improve the search and filter functionality.
