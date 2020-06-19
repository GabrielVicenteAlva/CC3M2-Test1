import glfw
from OpenGL.GL import *
from OpenGL.GLUT import *

vertices = [[0,0,0],[0,0,1],[0,1,1],[0,1,0],[1,0,0],[1,0,1],[1,1,1],[1,1,0]]

class Window:
	def __init__(self, width: int, height: int, title: str):
		# Initializing glfw library
		if not glfw.init():
			raise Exception('Glfw can not be initialized!')

		# Creating the window
		self._win = glfw.create_window(width, height, title, None, None)

		# Check if window was created
		if not self._win:
			glfw.terminate()
			raise Exception('Glfw window could not be created!')

		# Set window position
		glfw.set_window_pos(self._win, 400, 200)

		# Make the context current
		glfw.make_context_current(self._win)
		glClearColor(34/255, 34/255, 34/255, 1)  # 222222
		
		
		glfw.set_key_callback(self._win, self._keyPressed);
		self.rotate = False
		self.orientation = -45
		
	# Main application loop
	def main_loop(self):
		while not glfw.window_should_close(self._win):
			glfw.poll_events()
			glLoadIdentity()
			glScalef(.5,.5,.5)
			glRotatef(30,1, 0, 0) 
			glRotatef(self.orientation,0, 1, 0)
			glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
			#Dibujar Ejes
			self._draw_axes()
			if(self.rotate):
				glRotatef(30,1, 1, 1)
			glBegin(GL_LINES)
			glColor3f (1.0, .6, .6)
			self._draw_line(0,1)
			self._draw_line(1,2)
			self._draw_line(2,3)
			self._draw_line(3,0)
			glColor3f (0.6, 1.0, 0.6)
			self._draw_line(4,5)
			self._draw_line(5,6)
			self._draw_line(6,7)
			self._draw_line(7,4)
			glColor3f (0.6, 0.6 , 1.0)
			self._draw_line(0,4)
			self._draw_line(1,5)
			self._draw_line(2,6)
			self._draw_line(3,7)
			glEnd()

			glfw.swap_buffers(self._win)

		# Terminate glfw, free up allocated resources
		glfw.terminate()

	def _draw_line(self,a,b):
		glVertex3fv(vertices[a])
		glVertex3fv(vertices[b])
	
	def _draw_axes(self):
		glBegin(GL_LINES)
		glColor3f (1.0, 1.0, 0.0)
		glVertex3fv([0,0,0])
		glVertex3fv([3,0,0])
		glVertex3fv([0,0,0])
		glVertex3fv([0,3,0])
		glVertex3fv([0,0,0])
		glVertex3fv([0,0,3])
		glEnd()

	def _keyPressed(self,*args):
		if(args[1]==262):
			self.orientation += 3
		elif(args[1]==263):
			self.orientation -= 3
		elif(args[3]==1):
			self.rotate ^= 1
