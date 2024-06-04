def ASSIGNMENT(new_list, i, old_list, j):
    new_list[i] = old_list[j]


def mergeSort(list_to_sort_by_merge):
    if (
        len(list_to_sort_by_merge) > 1
        and not len(list_to_sort_by_merge) < 1
        and len(list_to_sort_by_merge) != 0
    ):
        mid = len(list_to_sort_by_merge) // 2
        left = list_to_sort_by_merge[:mid]
        right = list_to_sort_by_merge[mid:]

        mergeSort(left)
        mergeSort(right)

        l = 0
        r = 0
        i = 0

        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                ASSIGNMENT(new_list=list_to_sort_by_merge, i=i, old_list=left, j=l)
                l += 1
            else:
                ASSIGNMENT(new_list=list_to_sort_by_merge, i=i, old_list=right, j=r)
                r += 1
            i += 1

        while l < len(left):
            list_to_sort_by_merge[i] = left[l]
            l += 1
            i += 1

        while r < len(right):
            list_to_sort_by_merge[i] = right[r]
            r += 1
            i += 1


import matplotlib.pyplot as plt
import matplotlib.ticker as tck
import seaborn as sns

TITLE_SIZE = 18         #font size for plot titles
AX_LABEL_SIZE = 12      #font size for axis labels

my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
x = range(len(my_list))

#create two stacked sets of axes, draw unsorted list to top one, sorted list to the other one
fig, axes = plt.subplots(2, 1, figsize=(8, 6))

#plot and title unsorted list
sns.barplot(x=x, y=my_list, ax=axes[0])
axes[0].set_title("Unsorted List", fontsize=TITLE_SIZE)

#sort my_list
mergeSort(my_list)
x = range(len(my_list))     #generally not needed, but more resilient to failure of mergeSort function.

#plot and title sorted list
sns.barplot(x=x, y=my_list, ax=axes[1], color="red")
axes[1].set_title("Mergesorted List", fontsize=TITLE_SIZE)

#label axes and add grid to y axis:
for ax in axes:
    ax.set_xlabel("List index", fontsize=AX_LABEL_SIZE)
    ax.set_ylabel("List value", fontsize=AX_LABEL_SIZE)
    
    #Creating grid:
    ax.yaxis.set_minor_locator(tck.AutoMinorLocator(4))   
    ax.yaxis.grid(which="major", linestyle="dashed")
    ax.yaxis.grid(which="minor", linestyle="dotted")
    ax.set_axisbelow(True)                                  #put grid behind the plots
 
fig.tight_layout()  #needed to avoid intersection of titles and neighboring plots
plt.show()
