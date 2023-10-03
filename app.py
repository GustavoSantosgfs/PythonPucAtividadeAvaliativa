from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'supersecretkey'

DATABASE = 'database.db'

def query_db(query, args=(), one=False):
    with sqlite3.connect(DATABASE) as conn:
        cur = conn.cursor()
        cur.execute(query, args)
        rv = cur.fetchall()
        return (rv[0] if rv else None) if one else rv

@app.route('/')
def index():
    products = query_db('select * from products')
    return render_template('index.html', products=products)

@app.route('/add', methods=['POST'])
def add_product():
    if request.method == 'POST':
        code = request.form['code']
        name = request.form['name']
        price = request.form['price']
        with sqlite3.connect(DATABASE) as conn:
            conn.execute("INSERT INTO products (code, name, price) VALUES (?, ?, ?)", (code, name, price))
            conn.commit()
        flash('Product added successfully!')
    return redirect(url_for('index'))

@app.route('/update/<int:code>', methods=['GET', 'POST'])
def update_product(code):
    product = query_db('select * from products where code = ?', [code], one=True)
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        with sqlite3.connect(DATABASE) as conn:
            conn.execute("UPDATE products SET name = ?, price = ? WHERE code = ?", (name, price, code))
            conn.commit()
        flash('Product updated successfully!')
        return redirect(url_for('index'))
    return render_template('update_product.html', product=product)

@app.route('/delete/<int:code>')
def delete_product(code):
    with sqlite3.connect(DATABASE) as conn:
        conn.execute("DELETE FROM products WHERE code = ?", (code,))
        conn.commit()
    flash('Product deleted successfully!')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)