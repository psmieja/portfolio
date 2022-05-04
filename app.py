from flask import Flask, render_template, url_for
import json

app = Flask(__name__)

# a workaround solution to avoid boilerplate code in templates
# a method is made available in jinja templates that provides paths to icons
# which are all placed in the same directory and are named consistently
@app.context_processor
def utility_processor():
    def icon_path(tech):
        return f"/static/icons/{tech}-icon.png"
    return dict(icon_path=icon_path)


@app.route("/")
def home():
    with open("projects.json", "r") as f:
        projects = json.load(f)
    return render_template('projects.html', projects=projects)

if __name__ == '__main__':
    app.run(debug=True)