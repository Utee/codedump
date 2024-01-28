# app/routes.py

from flask import render_template, request, redirect, url_for, jsonify
from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/profile')
def profile():
    # You may fetch user data from the database or use a user session
    # For now, let's assume some dummy data
    user_data = {
        'full_name': 'John Doe',
        'age': 25,
        'gender': 'Male',
        'social_links': {
            'twitter': 'https://twitter.com/johndoe',
            'linkedin': 'https://www.linkedin.com/in/johndoe'
        },
        'profile_picture': 'path/to/profile_picture.jpg'
    }
    return render_template('profile.html', user_data=user_data)

@app.route('/logout')
def logout():
    # Implement your logout logic here (e.g., clearing session data)
    return redirect(url_for('index'))


@app.route('/upload', methods=['POST'])
def upload():
    # Handle file uploads and code processing
    # Redirect to the dashboard or any other page after processing
    return redirect(url_for('dashboard'))

@app.route('/settings', methods=['GET', 'POST'])
def settings():
    if request.method == 'POST':
        # Retrieve form data and update user settings
        full_name = request.form.get('full_name')
        age = request.form.get('age')
        gender = request.form.get('gender')
        social_links = request.form.get('social_links')
        profile_picture = request.form.get('profile_picture')

        # Update user settings in the database or session as needed

        # Redirect to the dashboard or any other page after updating settings
        return redirect(url_for('dashboard'))

    # Render the settings page for GET requests
    return render_template('settings.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '')

    # Perform the search logic based on the query
    # You might search for code, files, and images that are public on the platform

    # Dummy data for demonstration purposes
    search_results = [
        {'type': 'code', 'content': 'print("Hello, World!")'},
        {'type': 'file', 'content': 'example.txt'},
        {'type': 'image', 'content': 'example.jpg'},
    ]

    return render_template('search_results.html', query=query, results=search_results)


@app.route('/get_content/<content_id>')
def get_content(content_id):
    # Modify this function to load content based on content_id
    if content_id == 'profile-content':
        return render_template('profile.html')
    elif content_id == 'settings-content':
        return render_template('settings.html')
    elif content_id == 'upload-content':
        return render_template('upload.html')
    else:
        return jsonify({'error': 'Content not found'})

