mainApp.controller('studentController', function($scope) {
   $scope.student = {
      firstName: "colin",
      lastName: "sheppard",
      
      fullName: function() {
         var studentObject;
         studentObject = $scope.student;
         return studentObject.firstName + " " + studentObject.lastName;
      }
   };
});