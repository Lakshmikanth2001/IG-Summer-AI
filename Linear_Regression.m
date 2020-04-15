function [cost,weights]=Linear_Regression(x,y,alpha,epochs)
[rows,col]=size(x);
I=ones(rows,1);
x=[I x];
Theta=rand(col+1,1);
for i=1:epochs
    %schocaticated Gradient desent
    for j=1:rows
        y_predict=x(j,:)*Theta;
        error=y_predict-y(j);
        Theta=Theta-((alpha)*(x(j,:))*(error))';
        cost=((y_predict-y(j)).^2);
    end
end
weights=Theta;
cost=sum(((x*Theta)-(y)).^2);
end