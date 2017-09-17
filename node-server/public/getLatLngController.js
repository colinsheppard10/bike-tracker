angular.module('MyApp').controller('getLatLngController', ['$scope', '$http', 
	function($scope,$http) {
		$scope.getData = function() {
			var URL = "http://localhost:8081/getLatLng";
			$http.get(URL).then(function(response){
				console.log('back from server req');
				addMarker(response.data);
				displayLatlngRaw(response.data.lat,  response.data.lng);
			});
		}
	}
]);