function  F = mydct( f )
% 1D DCT transform
%   Input:
%       f: M-by-N matrix
%   Outpu:
%       F: M-by-N matrix
%
f = double(f);
[M, N] = size(f);
A = ones(M, N);
A(:,1) = 1/sqrt(2);
F = zeros(M, N);
for u=1:N
    B = cos((2*(1:N)-1)*pi*(u-1)/(2*N));
    F(:, u) = sum(sqrt(2/N)*A(:, u)*B.*f, 2);
end

end

