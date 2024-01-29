def check_bound(screen_size, offset, plot_coor, img_size, angle):
    def check_val(start_val, end_val, index):
        if start_val < 0:
            # Under
            output = plot_coor[index] + 1
        elif end_val > screen_size[index]:
            # Over
            output = plot_coor[index] - 1
        else:
            # In-Bound
            output = plot_coor[index]
        return output
    
    fast_delay = 1
    slow_delay = 100
    start_x = plot_coor[0] + offset[0]
    start_y = plot_coor[1] + offset[1]
    end_x = plot_coor[0] + img_size[0] - offset[0]
    end_y = plot_coor[1] + img_size[1] - offset[1]

    if start_x < 0 or start_y < 0 or end_x > screen_size[0] or end_y > screen_size[1]:
        # Out-Boundary
        angle = angle
        delay_time = fast_delay
        ori_x = check_val(start_x, end_x, 0)
        ori_y = check_val(start_y, end_y, 1)
    else:
        # In-Boundary
        angle += 1
        delay_time = slow_delay
        ori_x = check_val(start_x, end_x, 0)
        ori_y = check_val(start_y, end_y, 1)

    return (ori_x, ori_y), angle, delay_time
