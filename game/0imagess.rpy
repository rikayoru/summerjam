define config.mouse = {}

define config.mouse["default"] = [("gui/mouse1.png", 0,0)]

#************************************
# Фоны
#************************************CGs/common_album/common_1.webp

image bg wew1 = "BG/building1.png"
image bg wew2 = "BG/building2.png"
image bg wew3 = "BG/building3.png"

image bg lap = "BG/laptop.png" 
image bg nworld = "BG/newworld.png" 
image bg ofc1 = "BG/office1.png"
image bg ofc2 = "BG/office2.png"
image bg ghoome = "BG/wenthome.png"

# ************************************
# Постеры
# ************************************

image cg post2 = "BG/building4.png"
image cg post3 = "BG/building5.png"


#************************************
# Album Cover Images
#************************************



#************************************
# Персонажи
#************************************

# image mc normal = "images/side/side portr normal.png"
# image mc smile = "images/side/side portr smile.png"

# image jace augh = "images/char/jace/Jace augh.png"
# image jace awkward = "images/char/jace/Jace awkward.png"
# image jace downcast = "images/char/jace/Jace downcast.png"

# image adr annoyed = "images/char/adrian/Adrian annoyed.png"
# image adr awkward = "images/char/adrian/Adrian awkward.png"
# image adr nervous = "images/char/adrian/Adrian nervous.png"
# image adr smile = "images/char/adrian/Adrian smile.png"
# image adr surprised = "images/char/adrian/Adrian surprised.png"
#************************************
# Персонажи ПОДСВЕТКА
#************************************
image mc normal0 = At('side portr normal', sprite_highlight('portr'))
image mc smile0 = At('side portr smile', sprite_highlight('portr'))

image jace augh0 = At('jace augh', sprite_highlight('jace'))
#  = At('jace augh', sprite_highlight('jace'))
image jace awkward0 = At('jace awkward', sprite_highlight('jace'))
#  = At('jace awkward', sprite_highlight('jace'))
image jace downcast0 = At('jace downcast', sprite_highlight('jace'))
#  = At('jace downcast', sprite_highlight('jace'))
# images/char/hazel/hazel normal.png images/char/hazel/hazel smile.png

image hazel normal0 = At('hazel normal', sprite_highlight('hazel'))
image hazel smile0 = At('hazel smile', sprite_highlight('hazel'))


image adrian annoyed0 = At('adrian annoyed', sprite_highlight('adrian'))
image adrian awkward0 = At('adrian awkward', sprite_highlight('adrian'))
image adrian nervous0 = At('adrian nervous', sprite_highlight('adrian'))
image adrian smile0 = At('adrian smile', sprite_highlight('adrian'))
image adrian surprised0 = At('adrian surprised', sprite_highlight('adrian'))