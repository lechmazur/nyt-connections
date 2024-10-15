def do_two_lists_have_same_elements(list1, list2):
   #to lowercase
   list1 = [x.lower() for x in list1]
   list2 = [x.lower() for x in list2]
   if len(list1) != len(list2):
      return False
   return set(list1) == set(list2)


def run_eval(filep, all_extracted):
    used = set()
    scores = {}
    with open("/mnt/r/connections/results2/" + filep, 'r') as file:
        lines = file.read().strip().split('\n')
        total_score = 0
        count = 0
        index = 0
        while index < len(lines):
            try:
                num = int(lines[index].strip())
                used.add(num)
                groups = lines[index + 1:index + 5]
                index += 5  # Move to the next section

                # Process groups
                processed = []
                for g in groups:
                    # Remove text after '//' if any
                    g = g.split('//')[0]
                    # Remove text after ' - ' if any
                    g = g.split(' - ')[0]
                    splitg = g.split(',')
                    stripped = [
                        x.strip().strip('\'"')
                        .replace('1. ', '')
                        .replace('2. ', '')
                        .replace('3. ', '')
                        .replace('4. ', '')
                        .replace('<eos>', '')
                        for x in splitg
                    ]
                    # Remove text in parentheses
                    stripped = [x.split('(')[0].strip() for x in stripped]
                    # Handle colon ':' splitting
                    stripped = [
                        max(x.split(':'), key=lambda part: part.count(','))
                        if ':' in x else x
                        for x in stripped
                    ]
                    # Remove text before period '.' if any
                    stripped = [
                        x.split('.', 1)[1].strip()
                        if '.' in x and len(x.split('.', 1)) > 1 else x
                        for x in stripped
                    ]
                    # Remove text after dash '-' if any
                    stripped = [x.split(' - ')[0].strip() for x in stripped]
                    processed.append(stripped[:4])

                # Now compute the score
                compared_to = all_extracted[num].split('\n')
                score = 0
                for f in range(0, 4):
                    description = compared_to[f * 6]
                    words = compared_to[f * 6 + 1:f * 6 + 5]

                    match_found = False
                    for res in processed:
                        if do_two_lists_have_same_elements(res, words):
                            match_found = True
                            break

                    if match_found:
                        score += 1 / 4

                scores[num] = score
                total_score += score
                count += 1

            except ValueError:
                # If we can't convert to int, move to the next line
                index += 1
                continue

        print("Total score = ", total_score)
        print("Total count = ", count)
        print("Percentage = ", round(total_score / count * 100.0, 2))
    return used, list(scores.values())

