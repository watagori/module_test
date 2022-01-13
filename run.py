# 自作にしたパッケージを呼び出す
from view import viewParent
from view import viewChild
from model import modelParent
from model import modelChild

p_model = modelParent()
p_model.myName()

c_model = modelChild()
c_model.myName()

p_view = viewParent()
p_view.myName()

c_view = viewChild()
c_view.myName()
