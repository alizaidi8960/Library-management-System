from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Hardcoded credentials
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            return redirect(url_for('dashboard'))
        else:
            error = "Invalid username or password"
    return render_template('login.html', error=error)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        book_name = request.form.get('book_name')
        author_name = request.form.get('author_name')
        if not book_name or not author_name:
            error = "All fields are required"
            return render_template('add_book.html', error=error)
        success = f"Book '{book_name}' by {author_name} has been added!"
        return render_template('add_book.html', success=success)
    return render_template('add_book.html')

@app.route('/issue_book', methods=['GET', 'POST'])
def issue_book():
    if request.method == 'POST':
        book_name = request.form.get('book_name')
        issue_date = request.form.get('issue_date')
        return_date = request.form.get('return_date')
        if not book_name or not issue_date or not return_date:
            error = "All fields are required"
            return render_template('issue_book.html', error=error)
        success = f"Book '{book_name}' issued successfully!"
        return render_template('issue_book.html', success=success)
    return render_template('issue_book.html')

@app.route('/return_book', methods=['GET', 'POST'])
def return_book():
    if request.method == 'POST':
        book_name = request.form.get('book_name')
        serial_no = request.form.get('serial_no')
        if not book_name or not serial_no:
            error = "All fields are required"
            return render_template('return_book.html', error=error)
        success = f"Book '{book_name}' returned successfully!"
        return render_template('return_book.html', success=success)
    return render_template('return_book.html')

@app.route('/pay_fine', methods=['GET', 'POST'])
def pay_fine():
    if request.method == 'POST':
        fine_paid = request.form.get('fine_paid')
        if not fine_paid:
            error = "Fine must be paid to complete the process"
            return render_template('pay_fine.html', error=error)
        success = "Fine paid successfully!"
        return render_template('pay_fine.html', success=success)
    return render_template('pay_fine.html')

@app.route('/membership', methods=['GET', 'POST'])
def membership():
    if request.method == 'POST':
        membership_type = request.form.get('membership_type')
        if not membership_type:
            error = "Please select a membership type"
            return render_template('membership.html', error=error)
        success = f"Membership added for {membership_type}!"
        return render_template('membership.html', success=success)
    return render_template('membership.html')

@app.route('/reports')
def reports():
    return render_template('reports.html')

@app.route('/maintenance')
def maintenance():
    return render_template('maintenance.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)
