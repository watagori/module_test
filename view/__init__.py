# ここでどのモジュールのどのクラスをimportするか指定する
from .viewParent import viewParent as viewParent
from .viewChild import viewChild as viewChild

# ここにこのフォルダーに定義しているクラス名を列挙する
__all__ = ['viewParent', 'viewChild']
