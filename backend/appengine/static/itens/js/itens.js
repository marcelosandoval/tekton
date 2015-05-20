var itensModulo = angular.module('itensModulo',[]);

itensModulo.directive('itensform',function(){
    return{
        restrict: 'E',
        replace:true,
        templateUrl: '/static/itens/html/itens_form.html',
        scope:{
            item:'='
        },
        controller:function($scope,$http){
            $scope.salvandoFlag=false;
            $scope.salvar=function(){
                $scope.salvandoFlag=true;
                $http.post('/itenss/rest/new',$scope.item).success(function(item){
                    console.log(item);
                    $scope.item.nome ='';
                    $scope.item.tipo ='';
                    $scope.item.bonus ='';
                    $scope.item.passiva ='';
                    $scope.item.ativa='';
                    $scope.item.aura ='';
                    $scope.item.vlrCompra='';
                    $scope.item.vlrVenda='';
                    $scope.salvandoFlag=false;
                }).error(function(erros){
                    console.log(erros);
                    $scope.salvandoFlag=false;
                });
            }
        }
    };
});