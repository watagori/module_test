# ここでどのモジュールのどのクラスをimportするか指定する
from .modelParent import modelParent as modelParent
from .modelChild import modelChild as modelChild

# ここにこのフォルダーに定義しているクラス名を列挙する
__all__ = ['modelParent', 'modelChild']
