from app import app, extra_files

if __name__ == '__main__':
    app.run(host='0.0.0.0', extra_files=extra_files, debug=True)
