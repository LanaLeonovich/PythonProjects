from captcha.image import ImageCaptcha
pattern = 'SOMETHING'

captcha = ImageCaptcha(width=300, height=300)

captcha.write(pattern, "paptcha.png")

