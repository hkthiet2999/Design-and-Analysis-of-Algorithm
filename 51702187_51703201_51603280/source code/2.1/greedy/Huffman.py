#Libraries
import pylab
import time

#Khởi tạo class Cây nhị phân
class NodeTree(object):

	def __init__(self, left=None, right=None):
		self.left = left
		self.right = right

	def children(self):
		return (self.left, self.right)

	def nodes(self):
		return (self.left, self.right)

	def __str__(self):
		return '%s_%s' % (self.left, self.right)


# Main function implementing huffman coding
def huffman_code_tree(node, left=True, binString=''):
	if type(node) is str:
		return {node: binString}
	(l, r) = node.children()
	d = dict()
	d.update(huffman_code_tree(l, True, binString + '0'))
	d.update(huffman_code_tree(r, False, binString + '1'))
	return d

def main():
	freq = {}
	str = 'BCAADDDCCACACAC'
	
	startTime = time.time()
	#Tính tần số xuất hiện của mỗi ký tự (biến c) của chuỗi string cho trước
	for c in str:
		if c in freq:
			freq[c] += 1
		else:
			freq[c] = 1

	#Sắp xếp lại danh sách freq theo thứ tự các tần số giảm dần
	freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
	
	#Clone danh sách trên đặt tên là nodes
	nodes = freq

	while len(nodes) > 1:
		(key1, c1) = nodes[-1]
		(key2, c2) = nodes[-2]
		nodes = nodes[:-2]
		node = NodeTree(key1, key2)
		nodes.append((node, c1 + c2))

		nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

	huffmanCode = huffman_code_tree(nodes[0][0])

	print(' Char | Huffman code ')
	print('----------------------')
	for (char, frequency) in freq:
		print(' %-4r |%12s' % (char, huffmanCode[char]))
	
	runningTime = time.time() - startTime
	
	print("Running Time :", runningTime)

	pylab.plot([1,2,3],[4,5,7])
	pylab.show()
	pylab.plot([1,2,3],[4,5,7], 'o-')
	pylab.show()

main()