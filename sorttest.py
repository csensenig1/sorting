import sort

assert sort.sort([]) == []
assert sort.sort([1]) == [1]
assert sort.sort([1,2]) == [1,2]
assert sort.sort([2,1]) == [1,2]
assert sort.sort([1,2,3]) == [1,2,3]
assert sort.sort([1,3,2]) == [1,2,3]
assert sort.sort([2,1,3]) == [1,2,3]
assert sort.sort([2,3,1]) == [1,2,3]
assert sort.sort([1,2,3,4]) == [1,2,3,4]


assert sort.sort([5,4,2,9,7,8,1,3,6,0])==[0,1,2,3,4,5,6,7,8,9]
assert sort.sort([9,2,6,10,4,3,7,5,8,0,1])==[0,1,2,3,4,5,6,7,8,9,10]
assert sort.sort([11,10,3,1,2,4,8,5,9,7,0,6])==[0,1,2,3,4,5,6,7,8,9,10,11]
assert sort.sort([2,1,12,10,5,3,0,6,4,8,9,7,11])==[0,1,2,3,4,5,6,7,8,9,10,11,12]
assert sort.sort([3,11,0,8,1,5,7,6,13,2,4,9,10,12])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13]
assert sort.sort([8,2,10,12,4,1,5,11,14,0,13,6,9,3,7])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
assert sort.sort([11,3,14,4,1,2,13,15,5,8,9,7,0,10,6,12])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
assert sort.sort([7,4,12,2,0,5,15,10,11,6,13,9,16,8,1,3,14])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
assert sort.sort([1,13,14,4,0,17,6,7,15,16,11,9,2,10,3,12,5,8])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
assert sort.sort([6,8,12,3,2,17,0,9,7,1,5,18,10,16,15,4,13,14,11])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
assert sort.sort([12,10,16,0,1,9,11,13,15,19,4,3,2,14,6,18,8,17,5,7])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
assert sort.sort([13,9,18,4,8,10,0,11,2,19,15,16,6,12,20,14,17,5,1,3,7])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
assert sort.sort([1,12,17,18,15,19,13,11,7,8,6,10,21,4,16,14,3,2,5,20,0,9])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
assert sort.sort([7,10,5,13,1,19,2,12,3,15,18,20,16,22,11,9,17,0,21,14,4,6,8])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
assert sort.sort([13,16,9,2,21,15,4,20,8,14,3,6,7,10,5,17,0,11,22,12,18,1,23,19])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
assert sort.sort([17,5,22,1,23,2,20,19,14,0,9,6,18,8,13,24,10,4,12,15,11,7,16,21,3])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
assert sort.sort([9,8,21,3,13,14,2,25,10,4,6,15,7,19,1,11,22,0,23,17,12,5,20,24,18,16])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
assert sort.sort([23,4,2,17,12,9,1,11,22,21,19,7,10,3,15,5,0,20,13,24,14,8,25,26,16,18,6])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
assert sort.sort([3,9,25,21,17,26,12,10,16,14,4,0,27,20,22,1,8,11,13,23,18,5,7,6,24,15,2,19])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]
assert sort.sort([19,25,3,4,7,1,10,21,18,17,16,2,22,26,0,20,8,11,27,5,9,24,6,23,13,15,14,12,28])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]
assert sort.sort([14,24,15,23,10,6,19,28,5,26,12,18,21,7,11,3,25,27,9,13,16,20,17,29,4,1,22,0,2,8])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29]
assert sort.sort([14,8,22,30,2,11,20,12,5,21,19,23,17,29,6,4,10,27,13,16,3,0,1,15,24,26,18,9,28,25,7])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
assert sort.sort([15,13,10,3,2,23,22,11,16,20,26,12,7,17,24,5,6,1,28,30,21,19,14,9,27,0,8,25,18,4,31,29])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
assert sort.sort([2,23,19,32,14,27,9,3,30,10,11,18,7,4,0,24,25,21,12,6,17,31,15,13,8,29,26,28,1,22,16,5,20])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32]
assert sort.sort([22,9,6,7,23,11,29,19,4,24,8,14,13,12,2,1,32,28,18,5,21,15,30,33,3,16,31,0,25,20,26,27,17,10])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33]
assert sort.sort([26,20,7,34,11,8,18,22,33,19,15,27,5,1,3,30,21,32,0,23,2,28,17,4,12,14,16,25,29,13,10,9,31,6,24])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34]
assert sort.sort([1,34,33,23,24,21,14,2,18,26,0,16,10,6,20,4,3,27,5,19,12,25,7,11,9,35,15,31,28,32,8,29,17,22,30,13])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35]
assert sort.sort([14,6,9,2,8,5,32,11,7,13,3,21,26,28,17,4,36,33,23,34,31,19,16,29,0,12,30,1,18,24,35,20,10,27,15,25,22])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
assert sort.sort([1,9,17,5,25,15,34,28,16,2,29,21,8,4,13,18,36,37,27,26,12,20,35,30,11,22,19,7,31,10,0,33,24,23,32,14,6,3])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37]
assert sort.sort([12,8,31,19,32,1,3,16,14,35,38,37,4,17,30,9,20,10,18,13,28,36,23,15,2,6,29,21,22,34,7,11,33,27,24,5,0,26,25])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38]
assert sort.sort([23,37,20,13,25,22,7,14,6,19,9,12,0,3,4,5,10,18,17,16,8,36,11,15,1,2,21,34,27,31,35,28,29,30,32,38,33,24,26,39])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39]
assert sort.sort([5,15,18,32,37,29,35,1,30,6,13,31,0,7,11,27,19,26,33,2,17,8,40,38,4,28,23,10,12,25,24,39,16,21,14,20,3,36,9,22,34])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]
assert sort.sort([8,23,25,19,17,28,21,27,7,24,37,20,18,5,30,4,38,9,26,15,13,10,34,14,32,0,2,12,16,41,39,36,1,35,33,11,29,40,3,22,6,31])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41]
assert sort.sort([39,33,35,21,16,22,24,8,20,34,11,36,32,31,28,13,29,37,12,3,17,10,4,15,41,2,23,38,26,1,0,25,30,5,42,19,18,14,6,27,40,9,7])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42]
assert sort.sort([38,2,0,32,36,8,10,26,13,34,22,40,11,41,27,29,35,15,4,31,9,37,30,5,25,39,20,33,14,43,7,23,18,1,17,3,28,6,21,42,19,12,16,24])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43]
assert sort.sort([40,15,8,23,13,41,42,33,21,5,12,7,39,22,24,28,14,4,2,20,31,38,17,36,43,27,25,32,29,26,3,1,0,11,19,37,6,10,16,9,30,34,44,18,35])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44]
assert sort.sort([28,35,13,7,23,36,31,5,43,11,16,45,9,44,30,0,12,34,22,37,17,29,33,19,10,8,18,3,39,6,32,24,27,1,4,38,26,42,41,2,20,14,15,25,40,21])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45]
assert sort.sort([27,19,34,38,24,12,7,16,0,43,22,30,9,26,21,5,45,29,13,4,41,31,1,35,44,8,15,20,17,3,6,33,23,2,42,39,18,46,32,14,36,37,28,11,25,40,10])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46]
assert sort.sort([43,33,11,40,39,3,24,7,23,19,21,45,32,22,12,31,13,47,35,16,41,29,1,0,4,18,26,2,25,27,14,36,44,42,8,38,9,46,37,15,28,5,10,6,34,30,20,17])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47]
assert sort.sort([35,9,1,8,27,33,3,12,42,37,0,47,16,21,45,29,15,43,18,14,28,36,38,24,19,11,13,23,7,6,5,41,32,10,40,2,17,44,46,39,25,30,4,48,31,34,22,20,26])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48]
assert sort.sort([0,23,49,18,9,34,38,32,48,43,24,17,8,5,10,27,30,22,47,19,4,21,28,7,15,44,46,6,41,39,31,36,20,2,11,40,45,12,16,13,35,26,14,25,1,33,42,37,29,3])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49]
assert sort.sort([37,0,39,38,29,3,12,11,8,6,36,47,48,32,31,9,14,15,17,18,16,27,33,20,50,41,49,2,10,30,34,21,22,7,28,4,45,19,24,42,5,1,35,13,44,40,46,43,26,25,23])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
assert sort.sort([50,25,46,22,26,45,48,31,44,7,16,19,4,11,9,3,39,13,36,14,43,0,2,20,6,30,29,12,28,24,1,40,17,49,34,27,10,42,32,23,51,8,35,41,33,5,21,37,38,18,47,15])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51]
assert sort.sort([44,34,33,47,48,24,41,0,26,30,43,7,22,1,3,27,2,6,16,28,45,15,20,19,51,38,29,9,18,37,50,32,14,49,31,13,10,23,17,8,25,21,46,39,4,35,42,36,40,52,11,12,5])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52]
assert sort.sort([13,29,5,40,44,16,4,41,27,47,10,12,38,3,52,48,36,37,45,43,49,28,35,39,14,15,53,30,51,33,1,19,24,31,23,22,46,25,8,0,17,32,6,26,7,11,42,9,34,50,21,18,2,20])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53]
assert sort.sort([36,39,43,11,37,2,45,52,47,51,29,24,48,27,17,41,35,34,26,10,14,42,33,6,46,25,7,12,18,5,22,38,28,13,23,16,20,9,19,30,8,54,21,44,0,32,1,15,3,40,53,50,4,31,49])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54]
assert sort.sort([37,25,38,44,52,30,55,17,54,31,21,41,40,12,45,27,32,36,3,9,10,33,15,13,26,48,14,6,4,43,50,51,42,34,1,20,0,2,53,5,19,7,11,29,39,49,23,18,46,8,35,22,16,24,28,47])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55]
assert sort.sort([34,2,21,26,16,37,52,43,18,53,24,36,6,55,25,50,42,12,39,47,30,15,4,1,46,38,13,29,49,10,19,3,35,33,45,31,41,48,32,22,56,40,7,44,20,11,14,17,28,51,54,23,8,27,9,0,5])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56]
assert sort.sort([22,56,37,52,23,13,34,51,25,36,6,0,57,45,17,21,35,32,1,54,27,2,28,16,10,5,50,43,41,31,42,55,46,48,11,40,20,47,18,15,49,44,30,12,14,4,9,7,29,24,19,39,3,53,8,33,26,38])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57]
assert sort.sort([32,28,20,15,51,0,44,12,18,24,5,39,8,1,38,33,19,10,46,42,54,34,29,36,6,35,9,41,45,13,25,17,26,47,14,40,52,16,53,22,49,7,11,50,2,31,27,57,21,58,23,56,55,3,4,43,37,30,48])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58]
assert sort.sort([19,31,2,43,37,9,18,59,30,21,1,34,15,4,52,32,41,6,25,39,28,55,40,26,7,51,49,29,50,38,33,16,48,56,8,17,35,24,12,46,27,23,45,13,58,20,44,3,0,47,14,10,42,54,57,36,5,11,22,53])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59]
assert sort.sort([28,19,18,31,22,15,3,25,20,23,11,38,47,32,4,7,27,5,51,2,6,24,35,34,30,9,8,33,53,40,54,44,37,10,45,12,26,43,17,56,21,41,59,0,57,50,52,29,36,46,13,58,55,16,49,14,1,60,48,42,39])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60]
assert sort.sort([40,61,2,30,20,58,23,19,32,22,13,35,57,33,24,25,14,29,16,17,60,39,18,56,10,48,6,28,0,46,27,15,8,50,59,26,41,42,11,49,3,55,9,5,31,1,36,7,38,51,52,34,37,47,21,54,12,45,53,4,44,43])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61]
assert sort.sort([45,26,23,24,47,0,62,58,8,53,25,2,32,10,6,21,48,56,42,19,13,41,37,50,39,15,14,30,20,52,27,9,44,33,11,51,31,18,38,49,46,29,16,3,54,40,28,12,57,4,17,59,34,22,5,35,61,36,60,43,7,55,1])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62]
assert sort.sort([15,63,25,59,30,6,32,47,38,44,61,22,46,33,28,18,51,11,36,45,21,43,54,56,48,0,16,57,12,31,26,24,1,35,49,62,3,8,55,58,60,7,41,9,4,14,40,23,2,5,42,37,39,29,17,34,20,27,19,50,53,52,13,10])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63]
assert sort.sort([12,48,43,41,8,22,28,21,49,3,64,35,37,6,30,23,0,2,11,4,62,1,16,61,9,25,60,31,56,63,29,24,10,32,59,50,55,57,19,17,7,44,46,42,58,40,52,38,36,39,18,14,13,15,33,45,27,5,54,47,34,26,53,51,20])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64]
assert sort.sort([1,45,6,20,52,55,9,16,29,47,36,42,59,48,63,13,65,14,64,0,3,32,46,60,23,44,38,18,22,11,62,2,37,43,40,31,54,8,41,50,7,5,4,19,10,35,51,58,49,30,53,28,27,34,21,61,17,12,24,39,56,57,26,15,33,25])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65]
assert sort.sort([10,32,16,2,40,33,61,1,42,45,21,48,30,3,65,47,34,28,64,66,56,17,51,39,35,60,7,54,29,27,15,24,9,26,12,20,25,14,0,50,23,31,37,62,18,43,36,49,44,38,6,5,63,41,4,46,53,19,8,11,59,13,55,22,52,58,57])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66]
assert sort.sort([18,30,43,51,66,54,55,60,45,33,0,16,64,4,35,20,12,42,44,41,39,46,24,10,53,62,36,17,28,48,7,49,52,3,50,31,67,34,5,40,47,1,13,57,27,15,25,21,32,11,61,23,59,38,63,58,19,8,6,29,14,22,65,2,56,26,37,9])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67]
assert sort.sort([7,54,9,62,42,38,29,55,35,17,20,5,37,8,26,12,31,40,57,6,30,2,43,21,50,67,44,41,56,27,68,25,18,3,28,63,61,16,49,24,60,65,15,34,39,32,33,13,66,47,45,22,58,1,23,36,10,59,14,53,51,0,11,52,19,64,46,48,4])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68]
assert sort.sort([57,11,42,31,39,25,34,29,65,17,35,0,23,50,30,58,40,32,63,55,64,18,33,14,7,10,9,37,59,43,27,47,38,15,51,46,54,53,60,45,19,6,22,16,24,21,67,1,56,41,20,8,52,62,13,26,69,66,5,2,48,28,4,3,12,44,68,49,61,36])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69]
assert sort.sort([54,12,67,34,55,69,46,65,44,16,60,36,11,13,64,42,38,58,31,17,7,29,26,19,24,0,66,14,39,9,62,57,25,61,28,20,5,1,32,43,15,21,47,68,35,41,51,33,10,63,18,23,2,49,6,30,70,4,45,53,40,59,37,52,56,27,48,3,22,50,8])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70]
assert sort.sort([60,13,64,30,1,6,39,29,19,40,0,12,5,37,51,20,18,2,33,66,14,7,70,62,59,41,34,9,38,52,32,67,4,21,22,42,23,57,63,69,15,17,61,44,11,49,35,36,24,71,31,43,47,65,55,8,28,56,58,26,3,46,50,10,27,16,53,68,45,25,48,54])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71]
assert sort.sort([32,57,37,65,36,35,3,55,30,69,42,48,18,17,34,58,16,7,63,33,4,60,11,1,19,59,50,67,40,27,5,71,23,66,46,24,22,14,52,29,39,10,43,53,72,28,38,8,9,51,62,15,20,49,64,70,47,45,61,21,25,13,68,56,44,12,6,31,26,0,41,54,2])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72]
assert sort.sort([6,20,56,52,59,8,5,60,54,28,35,51,36,7,61,66,48,65,11,3,2,46,69,19,58,15,72,27,37,32,43,57,31,34,39,70,41,45,16,50,53,63,71,44,21,42,13,30,24,25,1,10,49,62,55,47,29,38,68,12,9,67,22,73,17,64,33,40,14,18,4,0,23,26])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73]
assert sort.sort([8,71,58,28,18,67,61,68,11,35,12,21,70,50,10,48,55,2,43,27,14,33,49,19,22,4,72,42,1,23,34,13,3,44,32,66,17,62,63,56,29,51,41,31,36,16,15,40,38,7,57,24,59,73,46,45,54,65,6,37,53,30,60,9,26,25,0,74,64,47,20,39,5,69,52])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74]
assert sort.sort([9,0,41,2,66,53,75,51,74,5,30,42,70,38,59,60,29,35,25,63,65,19,12,31,37,64,33,11,62,26,73,28,48,57,18,61,55,39,43,49,52,22,24,15,8,23,45,6,56,72,32,20,14,44,1,58,21,4,54,13,7,17,34,46,67,47,69,10,3,50,40,36,68,71,16,27])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75]
assert sort.sort([9,23,22,48,0,16,11,59,17,45,18,30,63,49,43,75,55,32,71,56,53,40,31,41,38,47,20,66,4,68,24,14,74,27,10,33,36,15,42,67,5,65,39,70,72,73,57,13,58,25,26,34,44,6,60,37,35,29,12,3,62,61,8,7,76,1,69,28,51,64,50,52,2,19,21,46,54])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76]
assert sort.sort([31,15,40,9,19,12,7,74,0,1,11,72,38,71,10,36,42,35,4,28,56,37,14,64,75,27,30,41,76,48,47,22,63,53,17,45,68,49,5,57,77,26,46,2,6,59,65,34,43,24,69,25,20,18,3,58,33,23,60,70,21,39,62,67,55,51,52,8,32,13,73,29,61,54,66,50,16,44])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77]
assert sort.sort([64,5,67,7,15,16,43,24,76,39,27,33,52,65,20,21,70,8,62,23,4,13,18,38,47,28,42,59,50,0,72,2,44,46,74,40,9,69,61,49,73,54,34,58,45,31,63,19,35,26,57,66,75,11,17,25,1,77,30,10,41,78,51,22,29,48,60,14,36,55,68,56,3,37,12,53,32,6,71])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78]
assert sort.sort([41,0,13,39,14,17,18,22,34,7,36,12,40,21,24,3,77,64,48,69,4,15,74,1,26,63,19,25,11,27,66,62,10,73,38,23,71,55,35,31,8,58,44,67,57,33,52,37,32,20,43,49,61,29,68,54,60,65,30,51,47,5,46,70,50,16,72,79,56,75,59,78,42,6,9,28,45,2,76,53])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79]
assert sort.sort([67,64,5,2,41,52,78,66,62,20,13,36,37,11,68,49,63,74,32,21,24,26,46,30,42,28,33,51,47,55,53,45,69,4,73,57,54,80,8,77,70,35,79,12,31,22,34,43,75,29,48,72,39,59,10,16,9,18,38,50,23,27,25,44,65,40,14,60,17,56,6,15,7,71,76,0,58,19,61,1,3])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80]
assert sort.sort([61,42,47,20,79,18,4,72,50,51,66,6,67,0,68,55,5,81,54,74,30,32,43,33,13,78,75,22,36,1,65,46,7,56,14,60,44,40,39,12,48,9,34,31,45,26,29,27,53,73,35,2,11,3,25,58,21,41,19,80,38,10,24,37,59,71,64,23,49,28,17,15,62,70,52,16,8,63,57,76,77,69])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81]
assert sort.sort([52,62,58,45,64,34,2,36,10,26,20,21,60,61,50,80,37,4,11,33,54,24,23,9,28,47,22,6,7,72,66,81,74,49,16,13,17,76,55,40,38,57,67,14,56,15,0,48,5,75,77,1,78,19,46,73,3,44,12,30,51,25,31,69,59,41,8,71,27,42,32,68,39,63,65,43,70,35,82,79,29,53,18])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82]
assert sort.sort([2,4,39,0,66,61,62,21,76,71,18,16,15,41,28,50,31,72,24,29,46,58,12,60,19,52,30,63,54,65,5,83,6,10,13,27,56,37,9,26,44,79,33,78,17,3,49,45,69,74,1,11,59,20,70,73,57,68,53,47,22,34,32,64,40,23,7,77,51,67,75,80,38,48,82,42,25,8,36,55,35,43,14,81])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83]
assert sort.sort([70,54,68,62,31,37,33,24,6,19,42,81,22,55,36,12,82,15,67,13,34,47,83,35,29,23,76,72,50,10,75,2,66,69,4,5,46,56,26,52,84,1,64,38,7,80,30,20,17,77,11,71,58,21,41,74,48,32,43,49,27,3,39,61,59,73,57,45,0,78,60,25,53,18,51,16,44,63,79,8,28,14,40,65,9])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84]
assert sort.sort([42,35,19,66,68,25,13,84,43,83,2,44,47,57,8,58,59,6,15,75,64,39,17,53,79,10,61,33,11,54,69,37,50,26,48,29,49,55,34,1,56,52,23,27,3,76,72,65,46,77,31,36,51,81,30,40,22,74,28,70,21,0,78,41,38,67,24,20,85,16,12,32,71,73,5,7,45,63,62,9,4,80,14,82,60,18])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85]
assert sort.sort([58,35,38,51,43,40,45,55,9,52,22,64,57,6,78,12,77,21,33,23,70,2,18,50,37,44,75,83,34,17,5,49,25,8,72,76,59,30,62,86,39,48,53,68,24,36,10,85,84,13,63,54,47,81,56,60,14,1,28,4,31,20,61,15,80,32,16,41,69,29,74,27,71,67,26,7,42,3,79,46,19,11,82,66,73,0,65])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86]
assert sort.sort([0,1,70,57,61,79,45,12,16,60,19,66,73,9,5,86,50,54,43,21,14,74,32,3,11,26,30,24,42,64,36,13,48,46,52,4,75,23,31,27,72,85,76,34,2,44,58,22,47,78,53,87,17,77,68,25,83,20,84,8,67,6,38,59,51,29,35,55,28,80,71,41,33,18,56,62,81,82,39,37,63,15,69,49,7,65,40,10])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87]
assert sort.sort([67,85,20,70,24,40,88,13,23,38,2,27,84,29,81,14,44,48,71,74,17,52,34,46,1,26,42,45,54,47,87,79,37,0,3,25,43,28,36,65,49,77,68,8,58,30,50,64,53,82,80,19,61,75,12,60,41,56,57,11,22,78,7,32,59,4,69,86,21,31,9,10,73,51,62,83,66,16,5,39,33,6,76,55,35,72,18,63,15])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88]
assert sort.sort([77,43,14,19,3,89,47,1,71,74,53,73,36,6,70,11,7,29,18,55,45,23,32,63,78,75,27,41,79,16,8,72,35,9,76,64,12,84,56,67,48,2,24,0,69,83,21,65,5,52,86,51,42,85,4,33,22,20,59,26,10,81,44,30,34,54,66,61,15,38,28,62,57,87,60,37,25,13,68,50,58,39,82,88,17,31,49,80,46,40])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89]
assert sort.sort([34,24,13,32,77,8,5,33,85,54,66,4,47,55,17,21,52,57,89,37,72,80,88,11,16,81,40,20,63,87,48,46,53,0,70,2,6,30,44,69,31,10,86,39,51,18,83,43,35,71,78,41,7,73,56,60,65,29,62,1,38,36,42,82,26,3,68,50,58,28,61,76,74,9,19,90,15,84,79,45,49,64,14,23,67,12,27,75,25,59,22])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90]
assert sort.sort([40,68,85,56,70,74,1,7,48,54,87,62,69,53,17,86,78,49,16,36,39,47,55,6,44,61,72,15,2,28,65,14,33,10,76,60,82,20,30,21,18,80,50,67,91,12,59,24,3,5,19,9,26,0,45,66,42,25,23,4,46,31,35,51,34,37,8,79,58,71,29,38,43,57,81,27,73,84,13,63,64,83,90,89,32,52,88,22,11,41,77,75])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91]
assert sort.sort([70,50,49,88,86,8,75,39,54,82,16,92,11,77,32,60,36,80,19,72,57,22,53,79,56,66,34,64,4,30,41,65,38,40,21,18,42,81,55,47,84,0,69,90,25,7,74,61,27,63,31,45,85,26,9,13,14,62,5,3,24,2,58,59,23,78,43,1,48,15,46,91,28,12,73,29,33,37,52,71,51,35,87,67,44,83,89,76,10,68,20,17,6])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92]
assert sort.sort([88,71,49,20,43,38,39,27,21,4,28,79,85,2,92,12,52,54,16,8,36,26,42,91,59,23,61,48,66,5,81,24,19,89,31,60,13,76,11,51,46,82,7,35,57,37,68,53,64,63,25,70,77,50,40,9,83,3,78,30,67,87,29,80,84,55,33,56,0,15,45,86,1,58,65,47,10,72,90,44,69,93,75,18,34,62,17,14,41,73,74,6,22,32])==[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93]
