angular.module('MyApp').controller('studentController2', ['$scope', '$http', 
	function($scope,$http) {
		$scope.getData = function() {
			// var defaultHttpConfig = {
		    //     // headers: {
		    //     //     'Content-Type': 'application/json',
		    //     //     'Accept': 'application/json'
		    //     // }
		    // };
			var URL = "http://localhost:8081/makeRequest";
			$http.get(URL).then(function(response){
				console.log('came back');
				$scope.total = response;
			});
		}
	}
]);