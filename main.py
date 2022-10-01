from flask import Flask, render_template
import utils


app = Flask(__name__)


@app.route("/")
def list_candidates():
    """Главная: все кандидаты."""
    candidates = utils.load_candidates_from_json("candidates.json")
    return render_template("list.html", candidates=candidates)


@app.route("/candidate/<int:candidate_id>")
def page_candidate(candidate_id):
    """Кандидат по id."""
    candidate = utils.get_candidate(candidate_id)
    return render_template("card.html", candidate=candidate)


@app.route("/search/<candidate_name>")
def get_candidates_by_name(candidate_name):
    """Поиск кандидата по имени."""
    candidates = utils.get_candidates_by_name(candidate_name)
    return render_template("search.html", candidates=candidates)


@app.route("/skill/<skill_name>")
def get_candidates_by_skill(skill_name):
    """Поиск кандидата по скилу."""
    candidates = utils.get_candidates_by_skill(skill_name)
    return render_template("skills.html", candidates=candidates, count_candidates=len(candidates))


app.run()
