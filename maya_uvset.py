# 导入 maya.cmds 模块
import maya.cmds as cmds

# 定义一个函数，用于获取输入名称的模型

def select_by_name(mod_field, *args):
    # 获取输入框中的模型名称
    source_uv_set = cmds.textField(mod_field, query=True, text=True)

    # 获取选中的所有模型
    cmds.select(source_uv_set)


# 定义一个函数，用于获取输入框中的 UV 集名称，并复制 UV 集
def copy_uv_set(source_field, target_field,  *args):
    # 获取输入框中的 UV 集名称
    source_uv_set = cmds.textField(source_field, query=True, text=True)
    target_uv_set = cmds.textField(target_field, query=True, text=True)

    # 获取选中的所有模型
    selected_objects = cmds.ls(selection=True)

    # 遍历每个模型
    for obj in selected_objects:

        # 将源 UV 集复制到目标 UV 集
        cmds.polyCopyUV(obj, uvSetNameInput=source_uv_set, uvSetName=target_uv_set, ch=1)


# 创建一个窗口，标题为“Copy UV Set”
window = cmds.window(title="Copy UV Set", widthHeight=(300, 150))

# 创建一个垂直布局
cmds.columnLayout()

# 创建一个文本标签，显示提示信息
cmds.text(label="输入要选择对象的名称，如要选择所有该名称前缀与后缀的对象，\n在名称前后加上*，例如*pSphere*")

# 创建一个输入框，用于输入要选择的模型名称，并赋值给变量
mod_field = cmds.textField(placeholderText="输入模型名称")

# 创建一个按钮，绑定复制 UV 集的函数，并传入输入框变量作为参数
cmds.button(label="select", command=lambda x: select_by_name(mod_field, ))

# 创建一个文本标签，显示提示信息
cmds.text(label="选择对象并输入源和目标UV集的名称。")

# 创建两个输入框，分别用于输入要复制的 UV 集和目标 UV 集的名称，并赋值给变量
source_field = cmds.textField(placeholderText="输入源uv集")
target_field = cmds.textField(placeholderText="输入目标uv集")

# 创建一个按钮，绑定复制 UV 集的函数，并传入输入框变量作为参数
cmds.button(label="Copy", command=lambda x: copy_uv_set(source_field, target_field))


# 显示窗口
cmds.showWindow(window)