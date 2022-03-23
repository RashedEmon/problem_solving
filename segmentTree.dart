void main(){
  List<int> number = [1,3,-2,8,-7];
  
  segmentTree(number,0,number.length-1);
}

int segmentTree(List<int> arr,int start,int end){
  
  if(start>end){
      return 0;
  }
  
  if(start==end){
    return arr[start];
  }
  int mid = (start+(end-start)/2).toInt();
  int sum= segmentTree(arr,start,mid)+segmentTree(arr,mid+1,end);
  print("($start-$end):$sum");
  return sum;
}
