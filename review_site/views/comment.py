# /**
#  * @author [Limm-jk]
#  * @email [201602057@cs-cnu.org]
#  * @create date 2020-12-06 20:12:13
#  * @modify date 2020-12-06 20:12:13
#  * @desc [댓글의 동작을 담당]
#  */
from flask import Blueprint, render_template, request, redirect

from model import *

bp = Blueprint('comment', __name__, url_prefix='/comment')

@bp.route('/<int:id>/delete')
def comment_delete(id):
    comment = Comment.query.get_or_404(id)
    db.session.delete(comment)
    db.session.commit()
    
    return redirect('/')