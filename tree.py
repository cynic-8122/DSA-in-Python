
class TreeNode:
	def __init__(self, data) :
		self.data = data
		self.children = []
		self.parent = None

	def add_child(self, data) :
		self.parent = self
		self.children.append(data)

	def get_level(self) :
		level = 0
		itr = self.parent
		while itr :
			level += 1
			itr = itr.parent

		return level 
	'''
	def print_tree(self) :
		spacing = self.get_level() * " "
		print(spacing + child)
		if self.children :
			while child in self.children :
				
				child.print_tree()
	'''
	def print_tree(self):
		spaces = ' ' * self.get_level() * 3
		prefix = spaces + "|__" if self.parent else ""
		print(prefix + self.data)
		if self.children:
			for child in self.children:
				child.print_tree()

def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))

    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Google Pixel"))
    cellphone.add_child(TreeNode("Vivo"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    root.print_tree()

if __name__ == '__main__' :
	build_product_tree()
