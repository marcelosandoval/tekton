var itensModulo = angular.module('itensModulo',['rest']);

itensModulo.directive('itensform',function(){
    return{
        restrict: 'E',
        replace:true,
        templateUrl: '/static/itens/html/itens_form.html',
        scope:{
            item:'=',
            saveComplete: '&'
        },
        controller:function($scope,ItemApi){
            $scope.salvandoFlag=false;
            $scope.salvar=function(){
                $scope.salvandoFlag=true;
                $scope.errors={};
                ItemApi.salvar($scope.item).success(function(item){
                    if($scope.saveComplete != undefined){
                        $scope.saveComplete({'item':item});
                    }
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
                    $scope.errors=erros;
                    console.log(erros);
                    $scope.salvandoFlag=false;
                });
            }
        }
    };
});


itensModulo.directive('itenslinha',function(){
    return{
        restrict: 'A',
        replace:true,
        templateUrl: '/static/itens/html/item_linha_tabela.html',
        scope:{
            item:'=',
            deleteComplete: '&'
        },
        controller:function($scope,ItemApi){
            $scope.ajaxFlag=false;
            $scope.deletar=function(){
                ItemApi.deletar($scope.item.id).success(function(){
                    $scope.ajaxFlag=true;
                    $scope.deleteComplete({'item':$scope.item});
                });
            }
        }
    };
});