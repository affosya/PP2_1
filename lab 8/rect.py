import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 15
    x, y = 0, 0
    mode = 'blue'  # Initial drawing color
    drawing_mode = 'brush'  # Can be 'brush', 'rect', 'circle', 'eraser'
    points = []
    start_pos = None  # Store the start position for shapes
    
    while True:
        
        pressed = pygame.key.get_pressed()
        
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            
            # Exit conditions
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                
                # Change mode based on key presses
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_e:
                    drawing_mode = 'eraser'
                elif event.key == pygame.K_c:
                    drawing_mode = 'circle'
                elif event.key == pygame.K_r:
                    drawing_mode = 'rect'
                elif event.key == pygame.K_b:
                    drawing_mode = 'brush'
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click: begin drawing
                    if drawing_mode != 'eraser':
                        start_pos = event.pos
                    else:
                        # Erase from current mouse position
                        erase(screen, event.pos, radius)
                elif event.button == 3:  # Right click: shrink radius (for brush)
                    radius = max(1, radius - 1)
            
            if event.type == pygame.MOUSEMOTION:
                if event.buttons[0]:  # Drawing with left button held
                    if drawing_mode == 'brush':
                        points.append(event.pos)
                    elif drawing_mode == 'eraser':
                        erase(screen, event.pos, radius)
        
        # Clear screen and redraw everything
        screen.fill((0, 0, 0))
        
        if drawing_mode == 'brush':
            # Draw points
            draw_points(screen, points, radius, mode)
        elif drawing_mode == 'rect' and start_pos:
            # Draw rectangle from start to current mouse position
            draw_rectangle(screen, start_pos, pygame.mouse.get_pos(), mode)
        elif drawing_mode == 'circle' and start_pos:
            # Draw circle from start to current mouse position
            draw_circle(screen, start_pos, pygame.mouse.get_pos(), mode)
        
        pygame.display.flip()
        clock.tick(60)

def draw_points(screen, points, radius, mode):
    for i in range(len(points) - 1):
        drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)

def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

def erase(screen, pos, radius):
    pygame.draw.circle(screen, (0, 0, 0), pos, radius)

def draw_rectangle(screen, start_pos, end_pos, mode):
    rect_width = abs(end_pos[0] - start_pos[0])
    rect_height = abs(end_pos[1] - start_pos[1])
    rect_x = min(start_pos[0], end_pos[0])
    rect_y = min(start_pos[1], end_pos[1])
    
    color = get_color(mode)
    pygame.draw.rect(screen, color, pygame.Rect(rect_x, rect_y, rect_width, rect_height), 2)

def draw_circle(screen, start_pos, end_pos, mode):
    radius = int(((start_pos[0] - end_pos[0])**2 + (start_pos[1] - end_pos[1])**2) ** 0.5)
    color = get_color(mode)
    pygame.draw.circle(screen, color, start_pos, radius, 2)

def get_color(mode):
    if mode == 'red':
        return (255, 0, 0)
    elif mode == 'green':
        return (0, 255, 0)
    elif mode == 'blue':
        return (0, 0, 255)
    return (255, 255, 255)  # Default color is white

if __name__ == '__main__':
    main()
