def merge_two_sorted_lists(head1, head2):
    head2_indx = 0
    
    for i in head1:
        if i > head2[head2_indx]:
            head1.insert(i, head2[head2_indx])
            head2_indx += 1