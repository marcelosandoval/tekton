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
            $scope.editandoFlag=false;
            $scope.itemEdicao={};
            $scope.deletar=function(){
                ItemApi.deletar($scope.item.id).success(function(){
                    $scope.ajaxFlag=true;
                    $scope.deleteComplete({'item':$scope.item});
                });
            };

            $scope.editar=function(){
                $scope.editandoFlag=true;
                $scope.itemEdicao.id=$scope.item.id;
                $scope.itemEdicao.nome=$scope.item.nome;
                $scope.itemEdicao.tipo=$scope.item.tipo;
                $scope.itemEdicao.bonus=$scope.item.bonus;
                $scope.itemEdicao.passiva=$scope.item.passiva;
                $scope.itemEdicao.ativa=$scope.item.ativa;
                $scope.itemEdicao.aura =$scope.item.aura;
                $scope.itemEdicao.vlrCompra=$scope.item.vlrCompra;
                $scope.itemEdicao.vlrVenda= $scope.item.vlrVenda;
            };
            $scope.cancelar=function(){
                $scope.editandoFlag=false;
            };
            $scope.completarEdicao=function(){
                ItemApi.editar($scope.itemEdicao).success(function(item){
                    $scope.item=item;
                    $scope.editandoFlag=false;
                });

            };

        }
    };
});