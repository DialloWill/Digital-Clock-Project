import pygame
import time

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Digital Clock")

# Load custom font (You can change this path to your desired font)
font = pygame.font.Font(None, 100)

# Function to draw a gradient background
def draw_gradient_background():
    for i in range(HEIGHT):
        color = (0, 0, i % 256)  # Gradient effect from black to blue
        pygame.draw.line(screen, color, (0, i), (WIDTH, i))

# Function to render the time
def render_time():
    current_time = time.localtime()
    hours = current_time.tm_hour
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

    # Convert to 12-hour format with AM/PM
    if hours >= 12:
        period = "PM"
        if hours > 12:
            hours -= 12
    else:
        period = "AM"
        if hours == 0:
            hours = 12
    
    time_str = f"{hours:02}:{minutes:02}:{seconds:02} {period}"

    # Render the shadowed time text (gray color)
    shadow_text = font.render(time_str, True, (50, 50, 50))
    shadow_rect = shadow_text.get_rect(center=(WIDTH // 2 + 5, HEIGHT // 2 + 5))  # Offset shadow
    screen.blit(shadow_text, shadow_rect)
    
    # Render the main time text (white color)
    text = font.render(time_str, True, (255, 255, 255))
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, text_rect)

    # Display the date below the time
    date_str = time.strftime("%A, %B %d, %Y")  # Format: "Day, Month Date, Year"
    date_text = font.render(date_str, True, (255, 255, 255))
    date_rect = date_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))
    screen.blit(date_text, date_rect)

# Main loop
running = True
while running:
    screen.fill((0, 0, 0))  # Fill the screen with black
    draw_gradient_background()  # Draw gradient background
    render_time()  # Render the time and date

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()  # Update the display
    pygame.time.Clock().tick(FPS)  # Set the frame rate

# Quit pygame
pygame.quit()
