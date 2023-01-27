import pgzrun

# Bird sprite initialized #####################
bird = Actor('bird')
bird.topright = 0, 10
bird.hit = False
###############################################

# Initialize new sprite below #################

###############################################

WIDTH = 500
HEIGHT = bird.height + 20

def draw():
  screen.clear()
  # Bird sprite #################################
  bird.draw()
  ###############################################
  # Add code to draw your new sprite ############

  ###############################################

def update():
  # Function call to bird animation #############
  bird_animation()
  ###############################################
  # Function call for your spirte's animation ###

  ###############################################

def on_mouse_down(pos):
  if bird.collidepoint(pos):
    set_bird_down()
  else:
    print("You missed me!")

# Bird animation functions ####################
def bird_animation():
  bird.left += 2

  if not bird.hit and bird.left % 32 < 16:
    bird.image = 'bird'
  elif not bird.hit:
    bird.image = 'bird2'

  if bird.left > WIDTH:
    bird.right = 0

def set_bird_down():
  bird.hit = True
  bird.image = 'bird3'
  sounds.eep.play()
  clock.schedule_unique(set_bird_normal, 1.0)

def set_bird_normal():
  bird.hit = False
  bird.image = 'bird'
###############################################

# Define a function for your spirte's animation

###############################################

pgzrun.go()