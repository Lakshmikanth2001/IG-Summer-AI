function [cost,weights]=LR_batch_train(x,y,alpha,epochs)
[rows,col]=size(x);
I=ones(rows,1);
x=[I x];
Theta=rand(col+1,1);
for i=1:epochs
    y_predict=x*Theta;
    error=y_predict-y;
    Theta=Theta-(alpha*(x')*(error));
    cost=sum((y_predict-y).^2);
end
weights=Theta;
end 