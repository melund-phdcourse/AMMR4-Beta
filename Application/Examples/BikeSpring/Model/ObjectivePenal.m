% Computes the pseudo-objective function penalized for side constraint
% violations

function [Fps] = ObjectivePenal(xmin,x,xmax)

penalty = 2;  % exterior penalty factor
Fps = objective(x);
for j=1:length(x)
    if xmin(j) > x(j)
        Fps = Fps*(1 + penalty*(xmin(j)-x(j))^2);
    end
    if x(j) > xmax(j)
        Fps = Fps*(1 + penalty*(xmin(j)-x(j))^2);
    end
end
