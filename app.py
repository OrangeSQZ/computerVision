from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 도서와 멤버를 저장할 딕셔너리 생성ls
books = {}
members = {}

@app.route('/')
def index():
    return render_template('index.html', books=books, members=members)

@app.route('/add_member', methods=['POST'])
def add_member():
    name = request.form['name']
    phone = request.form['phone']
    members[name] = phone
    return redirect(url_for('index'))

@app.route('/remove_member', methods=['POST'])
def remove_member():
    name = request.form['name']
    if name in members:
        del members[name]
    return redirect(url_for('index'))

@app.route('/add_book', methods=['POST'])
def add_book():
    title = request.form['title']
    books[title] = "대출 가능"
    return redirect(url_for('index'))

@app.route('/remove_book', methods=['POST'])
def remove_book():
    title = request.form['title']
    if title in books:
        del books[title]
    return redirect(url_for('index'))

@app.route('/borrow_book', methods=['POST'])
def borrow_book():
    member_name = request.form['member_name']
    book_title = request.form['book_title']
    if book_title in books and books[book_title] == "대출 가능":
        books[book_title] = f"대출 중 ({member_name})"
    return redirect(url_for('index'))

@app.route('/return_book', methods=['POST'])
def return_book():
    member_name = request.form['member_name']
    book_title = request.form['book_title']
    if book_title in books and books[book_title].startswith("대출 중") and books[book_title].endswith(member_name):
        books[book_title] = "대출 가능"
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
