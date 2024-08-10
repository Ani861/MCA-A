def reconstruct_path(ordered_part, jumbled_part):
    correct_order = ['Start', 'Clearing', 'River', 'Village', 'Cave']

    complete_path = []
    ordered_index = 0
    jumbled_index = 0

   
    for landmark in correct_order:
        if ordered_index < len(ordered_part) and ordered_part[ordered_index] == landmark:
            complete_path.append(landmark)
            ordered_index += 1
   
        elif jumbled_index < len(jumbled_part) and landmark in jumbled_part:
            complete_path.append(landmark)
            jumbled_index += 1

    return complete_path


ordered_part = ['Start', 'River']
jumbled_part = ['Clearing', 'Village', 'Cave']

final_path = reconstruct_path(ordered_part, jumbled_part)
print(final_path)
